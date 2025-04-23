from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode
import asyncio
import time

tracer = trace.get_tracer(__name__)

async def trace_process(span_name: str, func, *args, attributes=None, **kwargs):
    with tracer.start_as_current_span(span_name) as span:
        if attributes:
            for key, value in attributes.items():
                span.set_attribute(key, value)
        
        try:
            if asyncio.iscoroutinefunction(func):
                response = await func(*args, **kwargs)
            else:
                response = func(*args, **kwargs)
            return response

        except Exception as e:
            span.record_exception(e)
            span.set_status(Status(StatusCode.ERROR))
            span.add_event(f"Error occurred: {str(e)}")
            raise e
