from app.config.tracer import tracer
from app.config.tracer import trace

async def trace_process(span_name: str, func, *args, asyncr=False, attributes=None, **kwargs):
    with tracer.start_as_current_span(span_name) as span:
        if attributes:
            for key, value in attributes.items():
                span.set_attribute(key, value)
        try:
            if asyncr:
                response = await func(*args, **kwargs)
                return response
            return func(*args, **kwargs)
        except Exception as e:
            span.record_exception(e)
            span.set_status(trace.status.Status(trace.status.StatusCode.ERROR))
            raise
