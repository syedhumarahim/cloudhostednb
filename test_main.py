from main import get_driver_with_highest_avg_speed

def test_mclaren_mercedes():
    driver, lap, speed = get_driver_with_highest_avg_speed('McLaren Mercedes')
    assert driver.strip() == 'Norris'
    assert lap == 53
    assert speed == 256.100

def test_mercedes():
    driver, lap, speed = get_driver_with_highest_avg_speed('Mercedes')
    assert driver.strip() == 'Hamilton'
    assert lap == 53
    assert speed == 255.849

def test_nonexistent_team():
    driver, lap, speed = get_driver_with_highest_avg_speed('Bugatti')
    assert driver is None
    assert lap is None
    assert speed is None

if __name__ == "__main__":
    test_mclaren_mercedes()
    test_mercedes()
    test_nonexistent_team()
    print("All tests passed!")
