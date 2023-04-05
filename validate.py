class Error(ValueError):
    def __ini__(self, field, reason):
        super().__init__(f'{field}: {reason}')
        self.field = field
        self.reason = reason


    def start_request(request):
        if not request.driver_id:
            raise Error('driver_id', 'empty')
        