# General messages
INTERNAL_SERVER_ERROR = 'INTERNAL_SERVER_ERROR'
UNAUTHORIZED_TO_ACCESS_RESOURCE = 'UNAUTHORIZED_TO_ACCESS_RESOURCE'
UNAUTHORIZED = 'UNAUTHORIZED'

# User messages
USER_ALREADY_EXISTS = 'USER_ALREADY_EXISTS'
USERNAME_TOO_SHORT = 'USERNAME_TOO_SHORT'
USER_NOT_FOUND = 'USER_NOT_FOUND'
PASSWORD_TOO_SHORT = 'PASSWORD_TOO_SHORT'
USERNAME_INVALID = 'USERNAME_INVALID'
EMAIL_INVALID = 'EMAIL_INVALID'
USER_CREATION_SUCCESS = 'USER_CREATION_SUCCESS'
USER_DOESNT_EXIST = 'USER_DOESNT_EXIST'
ALL_USERS_DELETED = 'ALL_USERS_DELETED'
NO_COMMUNITY_ID_GIVEN = 'NO_COMMUNITY_ID_GIVEN'
PASSWORD_CHANGED = 'PASSWORD_CHANGED'
RESET_PASSWORD_MAIL_SENT = 'RESET_PASSWORD_MAIL_SENT'

# Auth messages
LOGIN_SUCCESS = 'LOGIN_SUCCESS'
WRONG_CREDENTIALS = 'WRONG_CREDENTIALS'
ACCESS_TOKEN_REVOKED = 'ACCESS_TOKEN_REVOKED'
REFRESH_TOKEN_REVOKED = 'REFRESH_TOKEN_REVOKED'
ACCESS_TOKEN_REFRESHED = 'ACCESS_TOKEN_REFRESHED'
OLD_PASSWORD_INCORRECT = 'OLD_PASSWORD_INCORRECT'
RESET_PASSWORD_HASH_INVALID = 'RESET_PASSWORD_HASH_INVALID'
PASSWORD_RESET = 'PASSWORD_RESET'

# Car messages
CAR_DELETED = 'CAR_DELETED'
CAR_DOESNT_EXIST = 'CAR_DOESNT_EXIST'

# Community messages
COMMUNIY_WITH_THIS_CAR_ALREADY_EXISTS = 'COMMUNIY_WITH_THIS_CAR_ALREADY_EXISTS'
COMMUNIY_DOESNT_EXIST = 'COMMUNIY_DOESNT_EXIST'
COMMUNIY_DELETED = 'COMMUNIY_DELETED'
COMMUNIY_LEFT_AND_DELETED = 'COMMUNIY_LEFT_AND_DELETED'
COMMUNIY_INVITATION_SENT = 'COMMUNIY_INVITATION_SENT'
COMMUNITY_INVITATION_ACCEPTED = 'COMMUNIY_INVITATION_ACCEPTED'
COMMUNITY_INVITATION_DECLINED = 'COMMUNITY_INVITATION_DECLINED'
COMMUNIY_LEFT_SUCCESSFULLY = 'COMMUNIY_LEFT_SUCCESSFULLY'
UNAUTHORIZED_TO_ACCEPT_COMMUNITY_INVITATION = 'UNAUTHORIZED_TO_ACCEPT_COMMUNITY_INVITATION'
COMMUNITY_INVITATION_ALREADY_ACCEPTED = 'COMMUNITY_INVITATION_ALREADY_ACCEPTED'
COMMUNITY_INVITATION_DOESNT_EXIST = 'COMMUNITY_INVITATION_DOESNT_EXIST'
USER_ALREADY_INVITED = 'USER_ALREADY_INVITED'
NOT_AUTHORIZED_TO_REMOVE_USER_FROM_COMMUNITY = 'NOT_AUTHORIZED_TO_REMOVE_USER_FROM_COMMUNITY'
CANNOT_CREATE_COMMUNITY_WITH_FOREIGN_CAR = 'CANNOT_CREATE_COMMUNITY_WITH_FOREIGN_CAR'

# Refuel messages
REFUEL_DOESNT_EXIST = 'REFUEL_DOESNT_EXIST'
REFUEL_DELETED = 'REFUEL_DELETED'
CANT_CHANGE_REFUEL_COMMUNITY = 'CANT_CHANGE_REFUEL_COMMUNITY'

# Tour messages
CANT_START_TOUR_WHEN_HAVING_UNFINISHED_TOURS_IN_COMMUNITY = 'CANT_START_TOUR_WHEN_HAVING_UNFINISHED_TOURS_IN_COMMUNITY'
TOUR_NOT_FOUND = 'TOUR_NOT_FOUND'
TOUR_HAS_ALREADY_BEEN_FINISHED = 'TOUR_HAS_ALREADY_BEEN_FINISHED'
CANNOT_UPDATE_SENSITIVE_TOUR_DATA_WHEN_TOUR_IS_ALREADY_PAYED_FOR = 'CANNOT_UPDATE_SENSITIVE_TOUR_DATA_WHEN_TOUR_IS_ALREADY_PAYED_FOR'
TOUR_DELETED = 'TOUR_DELETED'
CANNOT_DELETE_TOUR_WHEN_A_NEW_TOUR_HAS_ALREADY_STARTED = 'CANNOT_DELETE_TOUR_WHEN_A_NEW_TOUR_HAS_ALREADY_STARTED'
NO_TOUR_EXISTING = 'NO_TOUR_EXISTING'
PASSENGERS_MUST_BE_COMMUNITY_MEMBERS = 'PASSENGERS_MUST_BE_COMMUNITY_MEMBERS'
PASSENGER_LIST_CANNOT_BE_CHANGED_WHEN_FORCE_FINISHING_A_TOUR = 'PASSENGER_LIST_CANNOT_BE_CHANGED_WHEN_FORCE_FINISHING_A_TOUR'
END_KM_MUST_BE_GREATER_START_KM = 'END_KM_MUST_BE_GREATER_START_KM'

# Payoff messages
CANT_CREATE_PAYOFF_WHEN_UNFINISHED_TOURS_EXIST = 'CANT_CREATE_PAYOFF_WHEN_UNFINISHED_TOURS_EXIST'
CANT_CREATE_PAYOFF_WITHOUT_REFUELS_AND_TOURS = 'CANT_CREATE_PAYOFF_WITHOUT_REFUELS_AND_TOURS'
PAYOFF_DOESNT_EXIST = 'PAYOFF_DOESNT_EXIST'
DEBT_DOESNT_EXIST = 'DEBT_DOESNT_EXIST'

# Task messages
TASK_DELETED = 'TASK_DELETED'
TASK_DOESNT_EXIST = 'TASK_DOESNT_EXIST'
TASK_MUST_BE_EITHER_TIME_OR_KM_TRIGGERED = 'TASK_MUST_BE_EITHER_TIME_OR_KM_TRIGGERED'
TASK_KM_NEXT_INSTANCE_MUST_BE_HIGHER_THEN_CURRENT_KM = 'TASK_KM_NEXT_INSTANCE_MUST_BE_HIGHER_THEN_CURRENT_KM'
TASK_TIME_NEXT_INSTANCE_MUST_BE_HIGHER_THEN_CURRENT_TIME = 'TASK_TIME_NEXT_INSTANCE_MUST_BE_HIGHER_THEN_CURRENT_TIME'

# Task instance messages
TASK_INSTANCE_ALREADY_FINISHED = 'TASK_INSTANCE_ALREADY_FINISHED'

# Geocoding messages
NO_GEOCODING_RESULTS = 'NO_GEOCODING_RESULTS'

# Event messages
END_MUST_BE_AFTER_START = 'END_MUST_BE_AFTER_START'
EVENT_DOESNT_EXIST = 'EVENT_DOESNT_EXIST'
EVENT_DELETED = 'EVENT_DELETED'
TO_MUST_BE_AFTER_FROM = 'TO_MUST_BE_AFTER_FROM'
