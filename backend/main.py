from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/submit-form/")
async def submit_form(
    fullName: str = Form(...),
    email: str = Form(...),
    phoneNumber: str = Form(""),
    currentRole: str = Form(...),
    fieldOfStudyWork: str = Form(...),
    otherField: str = Form(""),
    yearsOfExperience: str = Form(""),
    communication: str = Form(""),
    teamwork: str = Form(""),
    problemSolving: str = Form(""),
    leadershipinitiative: str = Form(""),
    timeManagement: str = Form(""),
    adaptability: str = Form(""),
    conflictResolution: str = Form(""),
    emotionalIntelligence: str = Form(""),
    programmingSkills: str = Form(""),
    softwareTools: str = Form(""),
    networkingCybersecurity: str = Form(""),
    dataAnalysisAIML: str = Form(""),
    industrySpecificTools: str = Form(""),
    certifications: str = Form(""),
    upskillingOpportunities: str = Form(...),
    careerGuidance: str = Form(...),
    comments: str = Form("")
):
   
    return {"message": f"Thanks {fullName}, your response has been recorded"}
