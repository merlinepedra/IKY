# -*- encoding: utf-8 -*-
from flask import Blueprint, current_app, request, jsonify
from factories._celery import create_celery
from factories.configuration import api_keys_read, api_keys_write
home = Blueprint('home_views', __name__)


################################################
# Testing
################################################
@home.route("/testing", methods=["POST"])
def r_testing():
    result = request.get_json()
    print("JSON : ", result)
    return jsonify(result)


################################################
# Task List
################################################
# @home.route("/tasklist", methods=["POST"])
@home.route('/tasklist', methods=['GET'])
def r_tasklist():
    module_list = []
    for rule in current_app.url_map.iter_rules():
        if rule.endpoint != 'static':
            module_list.append(rule.rule[1:])
    return jsonify(modules=module_list)


################################################
# State
################################################
@home.route("/state/<task_id>/<task_app>")
def r_state(task_id, task_app):
    celery = create_celery(current_app)
    res = celery.AsyncResult(task_id).state
    return jsonify(state=res, task_id=task_id, task_app=task_app)


################################################
# Result
################################################
@home.route("/result/<task_id>")
def r_result(task_id):
    celery = create_celery(current_app)
    res = celery.AsyncResult(task_id).get()
    return jsonify(result=res)


################################################
# API Keys
################################################
@home.route("/apikey", methods=["POST"])
def r_apikey():
    if request.json:
        api_keys = request.get_json()
        keys = api_keys_write(api_keys)
    else:
        keys = api_keys_read()
    return jsonify(keys=keys)


################################################
# Fullcontact
################################################
@home.route("/fullcontact", methods=["POST"])
def r_fullcontact():
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Fullcontact - Detected Username : ", username, from_m)
    res = celery.send_task('modules.fullcontact.fullcontact_tasks.' +
                           't_fullcontact', args=(username, ))
    print("Fullcontact - Task : ", res.task_id)
    return jsonify(module="fullcontact", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Peopledatalabs
################################################
@home.route("/peopledatalabs", methods=["POST"])
def r_peopledatalabs():
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Peopledatalabs - Detected Username : ", username, from_m)
    res = celery.send_task('modules.peopledatalabs.peopledatalabs_tasks.' +
                           't_peopledatalabs', args=(username, ))
    print("Peopledatalabs - Task : ", res.task_id)
    return jsonify(module="peopledatalabs", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Github
################################################
@home.route("/github", methods=["POST"])
def r_github():
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Github - Detected Username : ", username, from_m)
    res = celery.send_task('modules.github.github_tasks.t_github',
                           args=(username, from_m))
    print("Github - Task : ", res.task_id)
    return jsonify(module="github", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# GhostProject
################################################
@home.route("/ghostproject", methods=["POST"])
def r_ghostproject():
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("GhostProject - Detected Username : ", username, from_m)
    res = celery.send_task(
        'modules.ghostproject.ghostproject_tasks.t_ghostproject',
                           args=(username, ))
    print("Ghostproject - Task : ", res.task_id)
    return jsonify(module="ghostproject", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Keybase
################################################
@home.route("/keybase", methods=["POST"])
def r_keybase():
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Keybase - Detected Username : ", username, from_m)
    res = celery.send_task('modules.keybase.keybase_tasks.t_keybase',
                           args=(username, from_m))
    print("Keybase - Task : ", res.task_id)
    return jsonify(module="keybase", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Twitter
################################################
@home.route("/twitter", methods=["POST"])
def r_twitter():
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Twitter - Detected Username : ", username, from_m)
    res = celery.send_task('modules.twitter.twitter_tasks.t_twitter',
                           args=(username, from_m))
    print("Twitter - Task : ", res.task_id)
    return jsonify(module="twitter", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Linkedin
################################################
@home.route("/linkedin", methods=["POST"])
def r_linkedin():
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Linkedin - Detected Username : ", username, from_m)
    res = celery.send_task('modules.linkedin.linkedin_tasks.t_linkedin',
                           args=(username, from_m))
    print("Linkedin - Task : ", res.task_id)
    return jsonify(module="linkedin", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Leaks
################################################
@home.route("/leaks", methods=["POST"])
def r_leaks():
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Leaks - Detected Username : ", username, from_m)
    res = celery.send_task('modules.leaks.leaks_tasks.t_leaks',
                           args=(username, ))
    print("Leaks - Task : ", res.task_id)
    return jsonify(module="leaks", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Darkpass
################################################
@home.route("/darkpass", methods=["POST"])
def r_darkpass():
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Darkpass - Detected Username : ", username, from_m)
    res = celery.send_task('modules.darkpass.darkpass_tasks.t_darkpass',
                           args=(username, ))
    print("Darkpass - Task : ", res.task_id)
    return jsonify(module="leaks", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Gitlab
################################################
@home.route("/gitlab", methods=["POST"])
def r_gitlab(username=None):
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Gitlab - Detected Username : ", username, from_m)
    res = celery.send_task('modules.gitlab.gitlab_tasks.t_gitlab',
                           args=(username, ))
    print("Gitlab - Task : ", res.task_id)
    return jsonify(module="gitlab", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Usersearch
################################################
@home.route("/usersearch", methods=["POST"])
def r_usersearch(username=None):
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Usersearch - Detected Username : ", username, from_m)
    res = celery.send_task('modules.usersearch.usersearch_tasks.t_usersearch',
                           args=(username, ))
    print("Usersearch - Task : ", res.task_id)
    return jsonify(module="usersearch", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# EmailRepIO
################################################
@home.route("/emailrep", methods=["POST"])
def r_emailrep(username=None):
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("EmailRep - Detected Username : ", username, from_m)
    res = celery.send_task('modules.emailrep.emailrep_tasks.t_emailrep',
                           args=(username, ))
    print("EmailRep - Task : ", res.task_id)
    return jsonify(module="emailrep", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# SocialScan
################################################
@home.route("/socialscan", methods=["POST"])
def r_socialscan(username=None):
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("SocialScan - Detected Username : ", username, from_m)
    res = celery.send_task('modules.socialscan.socialscan_tasks.t_socialscan',
                           args=(username, ))
    print("SocialScan - Task : ", res.task_id)
    return jsonify(module="socialscan", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Instagram
################################################
@home.route("/instagram", methods=["POST"])
def r_instagram(username=None):
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Instagram - Detected Username : ", username, from_m)
    res = celery.send_task('modules.instagram.instagram_tasks.t_instagram',
                           args=(username, ))
    print("Instagram - Task : ", res.task_id)
    return jsonify(module="instagram", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Tiktok
################################################
@home.route("/tiktok", methods=["POST"])
def r_tiktok(username=None):
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Tiktok - Detected Username : ", username, from_m)
    res = celery.send_task('modules.tiktok.tiktok_tasks.t_tiktok',
                           args=(username, ))
    print("Tiktok - Task : ", res.task_id)
    return jsonify(module="tiktok", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Sherlock
################################################
@home.route("/sherlock", methods=["POST"])
def r_sherlock(username=None):
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Sherlock - Detected Username : ", username, from_m)
    res = celery.send_task('modules.sherlock.sherlock_tasks.t_sherlock',
                           args=(username, ))
    print("Sherlock - Task : ", res.task_id)
    return jsonify(module="sherlock", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Tinder
################################################
@home.route("/tinder", methods=["POST"])
def r_tinder(username=None):
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Tinder - Detected Username : ", username, from_m)
    res = celery.send_task('modules.tinder.tinder_tasks.t_tinder',
                           args=(username, ))
    print("Tinder - Task : ", res.task_id)
    return jsonify(module="tinder", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Venmo
################################################
@home.route("/venmo", methods=["POST"])
def r_venmo(username=None):
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Venmo - Detected Username : ", username, from_m)
    res = celery.send_task('modules.venmo.venmo_tasks.t_venmo',
                           args=(username, ))
    print("Venmo - Task : ", res.task_id)
    return jsonify(module="venmo", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Skype
################################################
@home.route("/skype", methods=["POST"])
def r_skype(username=None):
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Skype - Detected Username : ", username, from_m)
    res = celery.send_task('modules.skype.skype_tasks.t_skype',
                           args=(username, ))
    print("Skype - Task : ", res.task_id)
    return jsonify(module="skype", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Searches
################################################
@home.route("/search", methods=["POST"])
def r_search(username=None):
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Search - Detected Username : ", username, from_m)
    res = celery.send_task('modules.search.search_tasks.t_search',
                           args=(username, ))
    print("Search - Task : ", res.task_id)
    return jsonify(module="search", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Tweetiment
################################################
@home.route("/tweetiment", methods=["POST"])
def r_tweetiment(username=None):
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    task_id = json_result.get("task_id", "")
    print("Tweetiment - Detected Username : ", username, from_m, task_id)
    res = celery.send_task('modules.tweetiment.tweetiment_tasks.t_tweetiment',
                           args=(username, task_id, from_m))
    print("Tweetiment - Task : ", res.task_id)
    return jsonify(module="tweetiment", task=res.task_id,
                   param=username, from_m=from_m)


################################################
# Reddit
################################################
@home.route("/reddit", methods=["POST"])
def r_reddit(username=None):
    celery = create_celery(current_app)
    json_result = request.get_json()
    username = json_result.get("username", "")
    from_m = json_result.get("from", "")
    print("Reddit - Detected Username : ", username, from_m)
    res = celery.send_task('modules.reddit.reddit_tasks.t_reddit',
                           args=(username, ))
    print("Reddit - Task : ", res.task_id)
    return jsonify(module="reddit", task=res.task_id,
                   param=username, from_m=from_m)
