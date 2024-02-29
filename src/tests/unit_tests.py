import pytest
from unittest.mock import patch, MagicMock
from src.api.business_logic import BusinessLogic


@pytest.fixture
def business_logic():
    return BusinessLogic()


def test_get_all_users_initial(business_logic):
    users = business_logic.get_all_users()
    assert len(users) == 1


def test_get_user_found(business_logic):
    user = business_logic.get_user(0)
    assert user is not None
    assert user['id'] == 0


def test_get_user_not_found(business_logic):
    user = business_logic.get_user(999)
    assert user is None


def test_create_user(business_logic):
    new_user = business_logic.create_user("Jane", "Doe", 1990, "user")
    assert new_user['id'] == 1
    assert new_user['first_name'] == "Jane"
    assert new_user['group'] == "user"


def test_update_user_existing(business_logic):
    updated_data = {"first_name": "Updated", "last_name": "User"}
    result = business_logic.update_user(0, updated_data)
    assert result is not None
    assert result['first_name'] == "Updated"


def test_update_user_not_found(business_logic):
    updated_data = {"first_name": "Nonexistent"}
    result = business_logic.update_user(999, updated_data)
    assert result is None


def test_delete_user_existing(business_logic):
    result = business_logic.delete_user(0)
    assert result == True
    assert business_logic.get_user(0) is None


def test_delete_user_not_found(business_logic):
    result = business_logic.delete_user(999)
    assert result == False
