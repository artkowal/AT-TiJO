from lab01_asercja.src.main import add, max_value, is_perfect

def test_addition():
    # Arrange
    first_number = 1
    second_number = 2

    # Act
    result = add(first_number, second_number)

    # Assert
    assert result == 3

# -------------------------------------------------------------

def test_max_value_none():
    # Arrange
    tab = None

    # Act
    result = max_value(tab)

    # Assert
    assert result is None

def test_max_value_empty():
    # Arrange
    tab = []

    # Act
    result = max_value(tab)

    # Assert
    assert result is None

def test_max_value_single_element():
    # Arrange
    tab = [6]

    # Act
    result = max_value(tab)

    # Assert
    assert result == 6

def test_max_value():
    # Arrange
    tab = [1,2,3,4]

    # Act
    result = max_value(tab)

    # Assert
    assert result == 4

# -------------------------------------------------------------

def test_is_perfect_true():
    # Arrange
    num = 28

    # Act
    result = is_perfect(num)

    # Assert
    assert result == True

def test_is_perfect_false():
    # Arrange
    num = 12

    # Act
    result = is_perfect(num)

    # Assert
    assert result == False

def test_is_perfect_negative():
    # Arrange
    num = -2

    # Act
    result = is_perfect(num)

    # Assert
    assert result == False

#---------------------------------------
test_addition()

test_max_value_none()
test_max_value_empty()
test_max_value_single_element()
test_max_value()

test_is_perfect_true()
test_is_perfect_false()
test_is_perfect_negative()


print("----------------------------------------")
print("All tests were completed successfully !!")
print("----------------------------------------")