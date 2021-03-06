# structureRepair
#
# Used by:
# Modules from group: Hull Repair Unit (25 of 25)
type = "active"
runTime = "late"
def handler(fit, module, context):
    amount = module.getModifiedItemAttr("structureDamageAmount")
    speed = module.getModifiedItemAttr("duration") / 1000.0
    fit.extraAttributes.increase("hullRepair", amount / speed)