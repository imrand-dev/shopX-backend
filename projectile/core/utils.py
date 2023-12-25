def full_name(instance):
    if instance.first_name and instance.last_name:
        return f"{instance.first_name} {instance.last_name}".strip()
    return instance.email