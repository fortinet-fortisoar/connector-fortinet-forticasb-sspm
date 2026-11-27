"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

LOGGER_NAME = 'forticasb-sspm'
REQUEST_TIMEOUT = 600
AUTH_API_ENDPOINT = '/api/v2/auth'
RISK_API_ENDPOINT = '/api/v2/risks'
IDENTITIES_API_ENDPOINT = '/api/v2/identities'
ACTIVITIES_API_ENDPOINT = '/api/v2/user-activities'
FILES_API_ENDPOINT = '/api/v2/files'
AUDIT_API_ENDPOINT = '/api/v2/audit'

SORT_ORDER = {
    "Ascending": "ASC",
    "Descending": "DESC"
}

TIME_SORT_FIELD ={
    "Activity Timestamp":"activity_ts",
    "Record Creation Timestamp":"created_at"
}

ACTIVITY_TYPES = {
    "File Viewed": "file_viewed",
    "File Deleted": "file_deleted",
    "File Moved": "file_moved",
    "File Copied": "file_copied",
    "File Downloded": "file_downloaded",
    "File Shared": "file_shared",
    "File Sharing Revoked": "file_sharing_revoked",
    "File Shared Internally": "file_shared_internally",
    "File Shared Externally": "file_shared_externally",
    "File Link Created": "file_link_created",
    "File Owner Changed": "file_owner_changed",
    "Login Success": "login_success",
    "Login Failure": "login_failure",
    "User Created": "user_created",
    "User Deleted": "user_deleted",
    "Group Created": "group_created",
    "Group Deleted": "group_deleted",
    "Group Assigned": "group_assigned",
    "Group Deassigned": "group_deassigned",
    "MFA Enabled":"mfa_enabled",
    "MFA Disabled": "mfa_disabled",
    "Password Reset": "password_reset",
    "Enabled Third Party": "enabled_third_party",
    "Disabled Third Party": "disabled_third_party",
    "Add Third Party Permissions": "add_third_party_permissions",
    "Remove Third Party Permissions": "remove_third_party_permissions",
    "Sensitivity Label Applied": "sensitivity_label_applied",
    "Sensitivity Label Removed": "sensitivity_label_removed",
    "Sensitivity Label Changed": "sensitivity_label_changed"
}
