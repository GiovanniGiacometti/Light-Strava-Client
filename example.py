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

    # Paginated

    print("----------")

    pages = 5
    per_page = 20

    ids = []

    for page in range(1, pages + 1):
        activities = client.get_activities(page=page, per_page=per_page)
        print(f"Page {page + 1}: {len(activities)} activities")
        ids.extend(list(map(lambda x: x.id, activities)))

    assert len(ids) == pages * per_page
    assert len(set(ids)) == len(ids)

    for i in range(len(activities) - 1):
        assert activities[i].start_date > activities[i + 1].start_date
