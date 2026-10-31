from pydantic import BaseModel, Field


class HousingInput(BaseModel):
    MedInc: float = Field(..., description="Median Income")
    HouseAge: float = Field(..., description="House Age")
    AveRooms: float = Field(..., description="Average Rooms")
    Population: float = Field(..., description="Population")

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "MedInc": 8.3252,
                "HouseAge": 41.0,
                "AveRooms": 6.9841,
                "Population": 322.0
            }]
        }
    }


class IrisInput(BaseModel):
    sepal_length: float = Field(..., alias="sepal length (cm)")
    sepal_width: float = Field(..., alias="sepal width (cm)")
    petal_length: float = Field(..., alias="petal length (cm)")
    petal_width: float = Field(..., alias="petal width (cm)")

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "examples": [{
                "sepal length (cm)": 5.1,
                "sepal width (cm)": 3.5,
                "petal length (cm)": 1.4,
                "petal width (cm)": 0.2
            }]
        }
    }


class SentimentInput(BaseModel):
    text: str = Field(..., description="Text review to analyze")

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "text": "The food was delicious and the service was wonderful!"
            }]
        }
    }