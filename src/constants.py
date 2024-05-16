from fastapi import status

common_responses = {
    status.HTTP_400_BAD_REQUEST: {
        "model": dict[str, str],
        "content": {
            "application/json": {
                "example": {"detail": "An error message explaining the specific issue."}
            }
        },
    },
    status.HTTP_401_UNAUTHORIZED: {
        "model": dict[str, str],
        "content": {
            "application/json": {
                "example": {"detail": "Unauthorized - The request requires user authentication"}
            }
        },
    },
    status.HTTP_403_FORBIDDEN: {
        "model": dict[str, str],
        "content": {
            "application/json": {
                "example": {
                    "detail": "Permission denied - "
                    "The client does not have permission to access the requested resource"
                }
            }
        },
    },
    status.HTTP_404_NOT_FOUND: {
        "model": dict[str, str],
        "content": {
            "application/json": {
                "example": {"detail": "XXX was not found"}
            }
        }
    },
    status.HTTP_422_UNPROCESSABLE_ENTITY: {
        "model": dict[str, str],
        "content": {
            "application/json": {
                "example": {
                    "detail": "Invalid input data. Please check the input fields for errors."
                }
            }
        },
    },
}
