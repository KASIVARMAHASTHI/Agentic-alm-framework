from pydantic import BaseModel


class AppConfig(BaseModel):
    app_name: str = "Agentic ALM Framework"
    environment: str = "development"
    approval_required_for_high_risk: bool = True


settings = AppConfig()
