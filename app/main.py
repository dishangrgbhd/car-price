from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth, routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

app = FastAPI(title="Car Price Prediction API")

# Linking the middleware
app.add_middleware(LoggingMiddleware)

# Linking the endpoints
app.include_router(routes_auth.router, tags = ['Authentication'])
app.include_router(routes_predict.router, tags = ['Prediction'])

# Monitoring using Prometheus
Instrumentator().instrument(app).expose(app)

# Exception handling
register_exception_handlers(app)