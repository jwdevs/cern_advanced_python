import datetime

import freezegun


@freezegun.freeze_time(datetime.date(2023, 5, 21))
def tomorrow():
    today = datetime.date.today()
    return today + datetime.timedelta(days=1)


def test_tomorrow():
    assert tomorrow() == datetime.date(2023, 5, 22)

# Output:
# 1 passed in 0.03s
