from strava_client.models.base import StravaBaseModel


class StravaGetTokenRequest(StravaBaseModel):
    """
    Model holding all information needed to get
    an access token from Strava API.

    Attributes:
        client_id:
            The ID of the application.
        client_secret:
            The secret key of the application.
        code:
            The code received from the authorization
            server.
        grant_type:
            The type of grant. This is always
            "authorization_code" for this application
    """

    client_id: int
    client_secret: str
    code: str
    grant_type: str = "authorization_code"  # This is the default value


class StravaGetTokenResponse(StravaBaseModel):
    """
    Model holding all information received
    when getting an access token from Strava API.
    It is used also when refreshing the token.

    The response contains more information
    than this model, but we're only interested
    in the access token, refresh token and
    expiration time.
    """

    access_token: str
    refresh_token: str
    expires_at: int


class StravaRefreshTokenRequest(StravaBaseModel):
    """
    Model holding all information needed to refresh
    an access token from Strava API.

    Attributes:
        client_id:
            The ID of the application.
        client_secret:
            The secret key of the application.
        refresh_token:
            The refresh token received from the
            authorization server.
        grant_type:
            The type of grant. This is always
            "refresh_token" for this application
    """

    client_id: int
    client_secret: str
    refresh_token: str
    grant_type: str = "refresh_token"  # This is the default value
