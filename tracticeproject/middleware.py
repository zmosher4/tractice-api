# middleware.py
import time
import logging

logger = logging.getLogger(__name__)


class RequestTimeLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        logger.info(f"Starting request to {request.path} [{request.method}]")

        response = self.get_response(request)

        duration = time.time() - start_time
        logger.info(
            f"Request to {request.path} [{request.method}] completed in {duration:.2f}s"
        )

        return response
