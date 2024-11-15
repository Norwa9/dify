from typing import Any, Literal, Optional, Union

from pydantic import BaseModel

from core.workflow.nodes.base import BaseNodeData
from core.workflow.nodes.metadata_entities import MetadataFilterConfig


class RerankingModelConfig(BaseModel):
    """
    Reranking Model Config.
    """

    provider: str
    model: str


class VectorSetting(BaseModel):
    """
    Vector Setting.
    """

    vector_weight: float
    embedding_provider_name: str
    embedding_model_name: str


class KeywordSetting(BaseModel):
    """
    Keyword Setting.
    """

    keyword_weight: float


class WeightedScoreConfig(BaseModel):
    """
    Weighted score Config.
    """

    vector_setting: VectorSetting
    keyword_setting: KeywordSetting


class MultipleRetrievalConfig(BaseModel):
    """
    Multiple Retrieval Config.
    """

    top_k: int
    score_threshold: Optional[float] = None
    reranking_mode: str = "reranking_model"
    reranking_enable: bool = True
    reranking_model: Optional[RerankingModelConfig] = None
    weights: Optional[WeightedScoreConfig] = None


class ModelConfig(BaseModel):
    """
    Model Config.
    """

    provider: str
    name: str
    mode: str
    completion_params: dict[str, Any] = {}


class SingleRetrievalConfig(BaseModel):
    """
    Single Retrieval Config.
    """

    model: ModelConfig


class KnowledgeRetrievalNodeData(BaseNodeData):
    """
    Knowledge retrieval Node Data.
    """

    type: str = "knowledge-retrieval"
    query_variable_selector: list[str]
    authorized_dataset_ids_variable_selector: Optional[Union[list[str], str]] = None
    # Filter Mode Selection e.g. 'must' or 'should' or 'must_not'
    filter_mode_to_metadata_filter_config_dict: Optional[dict[str, MetadataFilterConfig]] = None
    dataset_ids: list[str]
    retrieval_mode: Literal["single", "multiple"]
    multiple_retrieval_config: Optional[MultipleRetrievalConfig] = None
    single_retrieval_config: Optional[SingleRetrievalConfig] = None
