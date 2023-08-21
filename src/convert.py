import os
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlparse

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s
from dataset_tools.convert import unpack_if_archive

# https://www.kaggle.com/datasets/dataclusterlabs/construction-vehicle-images


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "Construction Vehicle"
    dataset_path = "APP_DATA/archive"
    bboxes_path = "APP_DATA/archive/Annotations/Annotations"
    bboxes_folder = "Annotations"
    batch_size = 30
    ds_name = "ds"
    images_ext = ".jpg"
    bboxes_ext = ".xml"

    def create_ann(image_path, img_info):
        labels = []

        info_height = img_info.height
        info_wight = img_info.width

        file_name = get_file_name(image_path)

        ann_path = os.path.join(curr_bboxes_path, file_name + bboxes_ext)

        if file_exists(ann_path):
            tree = ET.parse(ann_path)
            root = tree.getroot()

            img_height = int(root.find(".//height").text)
            img_wight = int(root.find(".//width").text)

            all_objects = root.findall(".//object")

            for curr_object in all_objects:
                name = curr_object.find(".//name").text
                obj_class = meta.get_obj_class(name)
                coords_xml = curr_object.findall(".//bndbox")
                for curr_coord in coords_xml:
                    if img_height == info_height:
                        left = float(curr_coord[0].text)
                        top = float(curr_coord[1].text)
                        right = float(curr_coord[2].text)
                        bottom = float(curr_coord[3].text)
                    else:
                        left = float(curr_coord[0].text) * img_height / img_wight
                        top = float(curr_coord[1].text) * img_wight / img_height
                        right = float(curr_coord[2].text) * img_height / img_wight
                        bottom = float(curr_coord[3].text) * img_wight / img_height

                    rect = sly.Rectangle(
                        left=int(left), top=int(top), right=int(right), bottom=int(bottom)
                    )
                    label = sly.Label(rect, obj_class)
                    labels.append(label)

        return sly.Annotation(img_size=(info_height, info_wight), labels=labels)

    obj_class_tractor = sly.ObjClass("tractor", sly.Rectangle)
    obj_class_truck = sly.ObjClass("truck", sly.Rectangle)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class_tractor, obj_class_truck])
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    for subfolder in os.listdir(dataset_path):
        if subfolder == bboxes_folder:
            continue

        curr_images_path = os.path.join(dataset_path, subfolder)
        curr_bboxes_path = os.path.join(bboxes_path, subfolder.lower())
        images_names = os.listdir(curr_images_path)

        progress = sly.Progress("Add in dataset {} data".format(subfolder), len(images_names))

        for images_names_batch in sly.batched(images_names, batch_size=batch_size):
            img_pathes_batch = [
                os.path.join(curr_images_path, image_name) for image_name in images_names_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [
                create_ann(image_path, img_info)
                for image_path, img_info in zip(img_pathes_batch, img_infos)
            ]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(images_names_batch))
    return project
