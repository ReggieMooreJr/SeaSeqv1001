from typing import Any, Optional
import httpx
import logging
from mcp.server.fastmcp import FastMCP

# =========================
# Logging Setup
# =========================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("weather-mcp")
logger.info("Weather MCP server started")
logger.info("Using httpx version: %s", httpx.__version__)  
logger.info("Reggie You are a genius" )

# =========================
# MCP Server Init
# =========================
mcp = FastMCP("weather")

# =========================
# Constants
# =========================
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-mcp/1.0"


# =========================
# HTTP Client Helper
# =========================
async def make_nws_request(url: str) -> Optional[dict[str, Any]]:
    """Make a request to the NWS API with logging + error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json",
    }

    logger.info(f"Requesting URL: {url}")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()

            data = response.json()

            logger.info(f"Success: {url}")
            return data

        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error for {url}: {e}")
        except httpx.RequestError as e:
            logger.error(f"Request error for {url}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error for {url}: {e}")

    return None


# =========================
# Formatting Helpers
# =========================
def format_alert(feature: dict) -> str:
    """Format a weather alert into readable text."""
    props = feature.get("properties", {})

    return f"""
Event: {props.get("event", "Unknown")}
Area: {props.get("areaDesc", "Unknown")}
Severity: {props.get("severity", "Unknown")}
Description: {props.get("description", "No description available")}
Instructions: {props.get("instruction", "No specific instructions provided")}
""".strip()


# =========================
# MCP Tools
# =========================
@mcp.tool()
async def get_alerts(state: str) -> str:
    """
    Get weather alerts for a US state.

    Args:
        state: Two-letter US state code (e.g. CA, NY)
    """
    state = state.upper().strip()

    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    logger.info(f"Fetching alerts for state: {state}")

    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."

    if not data["features"]:
        return f"No active alerts for {state}."

    alerts = [format_alert(f) for f in data["features"]]
    return "\n\n---\n\n".join(alerts)


@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """
    Get weather forecast for a location.

    Args:
        latitude: Latitude of location
        longitude: Longitude of location
    """
    logger.info(f"Fetching forecast for ({latitude}, {longitude})")

    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "Unable to fetch forecast grid data."

    try:
        forecast_url = points_data["properties"]["forecast"]
    except KeyError:
        logger.error("Missing forecast URL in points response")
        return "Invalid forecast data received."

    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "Unable to fetch forecast details."

    periods = forecast_data.get("properties", {}).get("periods", [])

    if not periods:
        return "No forecast periods available."

    output = []

    for p in periods[:5]:
        output.append(
            f"""
{p.get("name", "Unknown")}:
Temperature: {p.get("temperature", "N/A")}°{p.get("temperatureUnit", "")}
Wind: {p.get("windSpeed", "N/A")} {p.get("windDirection", "")}
Forecast: {p.get("detailedForecast", "No forecast available")}
""".strip()
        )

    return "\n\n---\n\n".join(output)