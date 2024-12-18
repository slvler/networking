from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api, reqparse, abort

import json

app = Flask("ExampleApi")
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('title', required=True, dest='sth')
parser.add_argument('uploadDate', type=int, required=False)

videos = {
    'videos1': {'title': 'hello world'},
    'videos2': {'title': 'matlab'}
}

def write_changes_to_file():
    global videos
    videos = {k: v for k, v in sorted(videos.items(), key=lambda video: video[1]['upload'])}
    with open('videos.json', 'w') as f:
        json.dumps(videos)


class Video(Resource):

    def get(self, video_id):

        if video_id == "":
            return videos
        return videos[video_id], 200

    def put(self, video_id):
        args = parser.parse_args()
        new_video = {'title': args['title']}
        videos[video_id] = new_video
        return {video_id: videos[video_id]}, 201


    def delete(self, video_id):
        if video_id not in videos:
            abort(404, message=f'Video {video_id} not found')

        del videos[video_id]
        return "", 204


class VideoSchedule(Resource):

    def get(self):
        return videos

    def post(self):
        args = parser.parse_args()
        new_video = {'title':  args['title']}
        video_id = max(int(v.lstrip('video')) for v in videos.keys()) + 1
        video_id = f'video{video_id}'
        videos[video_id] = new_video
        return videos[video_id], 201

api.add_resource(Video, '/videos/<video_id>')
api.add_resource(VideoSchedule, '/videos')

# app = Flask(__name__)
#
# @app.get('/')
# def index():
#     return "hello world"
#
#
#
# @app.route('/protected')
# def protected_assets():
#     session_token = request.headers["Authorization"].split(" ")[1]
#
#     try:
#         descope_client = DescopeClient(client_id=1233)
#         jwt_response = descope_client.validate_session(session)
#
#         response = make_response(
#             jsonify(
#                 {"message": "Secret code"}
#             )
#         )
#     except:
#         pass
#



if __name__ == "__main__":
    app.run(port=8080)