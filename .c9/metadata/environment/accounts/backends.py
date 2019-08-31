{"filter":false,"title":"backends.py","tooltip":"/accounts/backends.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":1,"column":0},"end":{"row":1,"column":30},"action":"remove","lines":["from django.db.models import Q"],"id":3,"ignore":true},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""]},{"start":{"row":3,"column":6},"end":{"row":3,"column":21},"action":"remove","lines":["CaseInsensitive"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":11},"action":"insert","lines":["Email"]},{"start":{"row":4,"column":7},"end":{"row":5,"column":4},"action":"remove","lines":["","    "]},{"start":{"row":4,"column":22},"end":{"row":4,"column":26},"action":"remove","lines":["of U"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["u"]},{"start":{"row":4,"column":30},"end":{"row":12,"column":4},"action":"remove","lines":["using a case-insensitive query to check a","    combination of the supplied email/username and password.","    To avoid the risk of having two users with similar usernames,","    distinguished only by letter case (e.g. 'john' and 'John'), consider","    updating your User model to save usernames as lower case entries to","    the database.","    This will ensure all usernames have unique spellings, and as a result,","    our case insensitive query will return a single result only.","    "]},{"start":{"row":4,"column":30},"end":{"row":4,"column":70},"action":"insert","lines":["an exact match on the email and password"]},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]},{"start":{"row":6,"column":35},"end":{"row":6,"column":44},"action":"remove","lines":["_or_email"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["`"]},{"start":{"row":8,"column":32},"end":{"row":9,"column":35},"action":"remove","lines":[" using the supplied username","        or email (case insensitive)"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":53},"action":"insert","lines":["` based off the email"]},{"start":{"row":8,"column":68},"end":{"row":9,"column":7},"action":"insert","lines":["","       "]},{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""]},{"start":{"row":12,"column":8},"end":{"row":13,"column":0},"action":"remove","lines":["# Filter all users by searching for a match by username/ email.",""]},{"start":{"row":12,"column":8},"end":{"row":13,"column":7},"action":"insert","lines":["try:","       "]},{"start":{"row":13,"column":12},"end":{"row":13,"column":15},"action":"remove","lines":["   "]},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"remove","lines":["s"]},{"start":{"row":13,"column":32},"end":{"row":25,"column":0},"action":"remove","lines":["filter(Q(username__iexact=username_or_email) |","                                    Q(email__iexact=username_or_email))","        if not users:","            return None","","        # Then get the first result of the query (which is your user).","        user = users[0]","        # If the password is correct, return user object","        if user.check_password(password):","            return user","","        return None",""]},{"start":{"row":13,"column":32},"end":{"row":21,"column":4},"action":"insert","lines":["get(email=username)","","            if user.check_password(password):","                return user","","            return None","        except User.DoesNotExist:","            return None","    "]},{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"remove","lines":["c"]},{"start":{"row":24,"column":62},"end":{"row":24,"column":63},"action":"remove","lines":["U"]},{"start":{"row":24,"column":62},"end":{"row":24,"column":63},"action":"insert","lines":["u"]},{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["        ",""]},{"start":{"row":29,"column":0},"end":{"row":30,"column":0},"action":"insert","lines":["",""]},{"start":{"row":31,"column":27},"end":{"row":32,"column":0},"action":"insert","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":35,"column":23},"end":{"row":35,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567287629566,"hash":"11996628bf9d241cc0faad36e6ccabb00d9f48ae"}