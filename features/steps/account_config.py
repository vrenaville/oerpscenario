from support import model, assert_equal, set_trace, puts
import datetime

@given('I create monthly periods on the fiscal year with reference "{fy_ref}"')
def impl(ctx, fy_ref):
    assert '.' in fy_ref, "please use the full reference (e.g. scenario.%s)" % fy_ref
    module, xmlid = fy_ref.split('.', 1)
    _model, id = model('ir.model.data').get_object_reference(module, xmlid)
    assert _model == 'account.fiscalyear'
    fy = model('account.fiscalyear').get(id)
    fy.read('period_ids')
    if not fy.period_ids:
        model('account.fiscalyear').create_period([fy.id], {}, 1)


@given('I set the following currency rates')
def impl(ctx):
    for row in ctx.table:
        date = datetime.date.today().strftime(row['date'])
        currency = model('res.currency').get([('name', '=', row['currency'])])
        curr_rate = model('res.currency.rate').browse([('name', '=', date), ('currency_id', '=', currency.id)])
        if not curr_rate:
            puts('creating new rate')
            values = {'name': date, 'currency_id': currency.id, 'rate': row['rate']}
            model('res.currency.rate').create(values)
        else:
            curr_rate[0].rate = row["rate"]



@given('I allow cancelling entries on all journals')
def impl(ctx):
    for jrn in model('account.journal').browse([]):
        jrn.write({'update_posted': True})

@given(u'I have the module account installed')
def impl(ctx):
    assert model('ir.module.module').get(['name = account', 'state = installed'])

@given(u'no account set')
def impl(ctx):
    assert model('account.account').get([]) is None

@given(u'I want to generate account chart from chart template named "{name}" with "{digits}" digits')
def impl(ctx, name, digits=0):
    assert False
