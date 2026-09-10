from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.space_satellite_orbit_planner.models import AgenticSpaceSatelliteOrbitPlannerSession, AgenticSpaceSatelliteOrbitPlannerItem
from app.domain.space_satellite_orbit_planner.schemas import AgenticSpaceSatelliteOrbitPlannerSessionCreate, AgenticSpaceSatelliteOrbitPlannerItemCreate

class AgenticSpaceSatelliteOrbitPlannerService:
    @staticmethod
    def create_session(db: Session, data: AgenticSpaceSatelliteOrbitPlannerSessionCreate) -> AgenticSpaceSatelliteOrbitPlannerSession:
        db_obj = AgenticSpaceSatelliteOrbitPlannerSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticSpaceSatelliteOrbitPlannerSession:
        return db.query(AgenticSpaceSatelliteOrbitPlannerSession).filter(AgenticSpaceSatelliteOrbitPlannerSession.id == session_id).first()
