def decimal_to_binary(user):
    while user>=1:
        a=user%2
        print a
        b=user/2
        user=b
decimal_to_binary(13)