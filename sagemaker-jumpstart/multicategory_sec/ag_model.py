from sagemaker.estimator import Framework
from sagemaker.predictor import Predictor
from sagemaker.mxnet import MXNetModel
from sagemaker import image_uris
from sagemaker.serializers import CSVSerializer
from sagemaker.deserializers import JSONDeserializer


class AutoGluonTraining(Framework):
    def __init__(
        self,
        entry_point,
        region,
        framework_version,
        instance_type,
        source_dir=None,
        hyperparameters=None,
        **kwargs,
    ):
        image_uri = image_uris.retrieve(
            "autogluon",
            region=region,
            version=framework_version,
            py_version="py37",
            image_scope="training",
            instance_type=instance_type,
        )
        super().__init__(
            entry_point,
            source_dir,
            hyperparameters,
            instance_type=instance_type,
            image_uri=image_uri,
            **kwargs,
        )

    def _configure_distribution(self, distributions):
        return

    def create_model(
        self,
        model_server_workers=None,
        role=None,
        vpc_config_override=None,
        entry_point=None,
        source_dir=None,
        dependencies=None,
        image_name=None,
        **kwargs,
    ):
        return None


class AutoGluonTabularPredictor(Predictor):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, serializer=CSVSerializer(), deserializer=JSONDeserializer(), **kwargs
        )


class AutoGluonInferenceModel(MXNetModel):
    def __init__(
        self, model_data, role, entry_point, region, framework_version, instance_type, **kwargs
    ):
        image_uri = image_uris.retrieve(
            "autogluon",
            region=region,
            version=framework_version,
            py_version="py37",
            image_scope="inference",
            instance_type=instance_type,
        )
        super().__init__(
            model_data, role, entry_point, image_uri=image_uri, framework_version="1.8.0", **kwargs
        )