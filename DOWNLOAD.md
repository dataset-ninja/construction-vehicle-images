Dataset **Construction Vehicle Images** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE1OTlfQ29uc3RydWN0aW9uIFZlaGljbGUgSW1hZ2VzL2NvbnN0cnVjdGlvbi12ZWhpY2xlLWltYWdlcy1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICIwK0E5Qm8vVFpxNERmZzVQZCs0NzNMWERycmk4bkpscWhydFJ4T2tTVDlNPSJ9)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Construction Vehicle Images', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/dataclusterlabs/construction-vehicle-images/download?datasetVersionNumber=2).