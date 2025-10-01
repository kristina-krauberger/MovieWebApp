from flask import abort

def get_valid_user_or_abort(data_manager, user_id):
    user = data_manager.get_user(user_id)
    if not user:
        abort(404, description="User not found.")
    return user


def get_valid_movie_or_abort(data_manager, movie_id):
    movie = data_manager.get_movie(movie_id)
    if not movie:
        abort(404, description="Movie not found.")
    return movie