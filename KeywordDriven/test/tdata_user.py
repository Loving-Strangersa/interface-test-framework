from public.random_data import faker

tdata_user_login_succeed = {
    "step_user_register": {"username": faker.random_password,
                           "pwd": faker.random_password,
                           "nickname": faker.random_password,
                           },
    "step_user_login": {
        "!username": "step_user_register username",
        "!pwd": "step_user_register pwd"
    }
}
