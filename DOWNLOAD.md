Dataset **Construction Vehicle Images** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/f/3/ZU/YRvZtsxH9oqpvt6ntB16BoZvFDv1q8vFlLbHLwhUPHdg2qaSCyHsecqZLzBeYtct72Ew6FjRS50DgPK49wlNxQY4vEeHRDYRtICiCDoOGF35j0npoBypX0qftfhu.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Construction Vehicle Images', dst_path='~/dtools/datasets/Construction Vehicle Images.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/dataclusterlabs/construction-vehicle-images/download?datasetVersionNumber=2)