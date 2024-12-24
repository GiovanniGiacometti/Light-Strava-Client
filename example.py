from datetime import datetime
from strava_client.client import StravaClient


if __name__ == "__main__":
    client = StravaClient()

    per_page = 20
    activities = client.get_activities(per_page=per_page)

    assert len(activities) == per_page

    for activity in activities[:2]:
        print(
            f"{activity.name} - {activity.sport_type.value}: {activity.distance}m on {activity.start_date}"
        )

    print("----------")

    # get activities done on a specific date
    base_date = "2024-12-24"

    start = datetime.strptime(f"{base_date} 00:00:00", "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(f"{base_date} 23:59:59", "%Y-%m-%d %H:%M:%S")

    activities = client.get_activities(before=end, after=start, per_page=per_page)

    # this holds for me :)
    assert len(activities) == 1, len(activities)

    for activity in activities:
        print(
            f"{activity.name} - {activity.sport_type.value}: {activity.distance}m on {activity.start_date}"
        )
