from fastapi import FastAPI

app=FastAPI(                                   
    title="Splitwise Clone API",
    version="0.1.0",    
)    
#Create the application instance. Uvicorn will look for this object named app.

@app.get("/health")
def health_check():
    return{'status':'ok'}
