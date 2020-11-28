from marshmallow import Schema, fields,post_load,validates,ValidationError


class norline(object):
    def __init__(self, xaxis,yaxis,typelist,maintitle,mintitle):
        self.xaxis = xaxis
        self.yaxis = yaxis
        self.typelist = typelist
        self.maintitle = maintitle
        self.mintitle = mintitle

class norlineSchema(Schema):
    xaxis = fields.List(fields.String(),required=True)
    yaxis = fields.List(fields.Float(),required=True)
    typelist = fields.List(fields.String(),required=True)
    maintitle = fields.Str(required=True)
    mintitle = fields.Str(required=False)
    @validates('xaxis')
    def validate_filename(self, value):
        if len(value) == 0:
            raise ValidationError('xaxis is null.')
    @validates('yaxis')
    def validate_classname(self, value):
        if len(value) == 0:
            raise ValidationError('yaxis is null.')
    @validates('typelist')
    def validate_classname(self, value):
        if len(value) == 0:
            raise ValidationError('typelist is null.')
    @validates('maintitle')
    def validate_classname(self, value):
        if len(value) == 0:
            raise ValidationError('maintitle is null.')
    @validates('mintitle')
    def validate_classname(self, value):
        pass
    @post_load
    def make_user(self,data, **kwargs):
        return norline(**data)


class mulline(object):
    def __init__(self, xaxis,yaxis,typelist,maintitle,mintitle):
        self.xaxis = xaxis
        self.yaxis = yaxis
        self.typelist = typelist
        self.maintitle = maintitle
        self.mintitle = mintitle

class mullineSchema(Schema):
    xaxis = fields.List(fields.String(),required=True)
    yaxis = fields.List(fields.List(fields.Float()),required=True)
    typelist = fields.List(fields.String(),required=True)
    maintitle = fields.Str(required=True)
    mintitle = fields.Str(required=False)
    @validates('xaxis')
    def validate_filename(self, value):
        if len(value) == 0:
            raise ValidationError('xaxis is null.')
    @validates('yaxis')
    def validate_classname(self, value):
        if len(value) == 0:
            raise ValidationError('yaxis is null.')
    @validates('typelist')
    def validate_classname(self, value):
        if len(value) == 0:
            raise ValidationError('typelist is null.')
    @validates('maintitle')
    def validate_classname(self, value):
        if len(value) == 0:
            raise ValidationError('maintitle is null.')
    @validates('mintitle')
    def validate_classname(self, value):
        pass
    @post_load
    def make_user(self,data, **kwargs):
        return mulline(**data)
