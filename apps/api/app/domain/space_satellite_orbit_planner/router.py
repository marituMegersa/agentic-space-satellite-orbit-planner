from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.space_satellite_orbit_planner.schemas import AgenticSpaceSatelliteOrbitPlannerSessionCreate, AgenticSpaceSatelliteOrbitPlannerSessionResponse
from app.domain.space_satellite_orbit_planner.service import AgenticSpaceSatelliteOrbitPlannerService

router = APIRouter(prefix="/api/v1/space_satellite_orbit_planner", tags=["Agentic Space Satellite Orbit Planner Domain"])

@router.post("/sessions", response_model=AgenticSpaceSatelliteOrbitPlannerSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticSpaceSatelliteOrbitPlannerSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Space Satellite Orbit Planner.
    """
    return AgenticSpaceSatelliteOrbitPlannerService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticSpaceSatelliteOrbitPlannerSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticSpaceSatelliteOrbitPlannerService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
