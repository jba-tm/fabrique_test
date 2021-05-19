from django_filters import OrderingFilter as BaseOrderingFilter


class OrderingFilter(BaseOrderingFilter):
    def __init__(self, *args, **kwargs):
        """
        ``fields`` may be either a mapping or an iterable.
        ``field_labels`` must be a map of field names to display labels
        """
        fields = kwargs.pop('fields', {})
        fields = self.normalize_fields(fields)
        field_labels = kwargs.pop('field_labels', {})

        self.param_map = {v: k for k, v in fields.items()}

        if 'choices' not in kwargs:
            kwargs['choices'] = self.build_choices(fields, field_labels)

        kwargs.setdefault('label', 'Ordering')
        kwargs.setdefault('help_text', '')
        kwargs.setdefault('null_label', None)
        super().__init__(*args, **kwargs)


