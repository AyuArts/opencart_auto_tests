def validate_option(allowed_values):
    def decorator(func):
        def wrapper(self, option_sort, *args, **kwargs):
            if option_sort not in allowed_values:
                self.log.warning(
                    f"[VALIDATION] value '{option_sort}' notAllowed. "
                    f"Permissible values: {allowed_values}"
                )
                return False
            return func(self, option_sort, *args, **kwargs)

        return wrapper

    return decorator
