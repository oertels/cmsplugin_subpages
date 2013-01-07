from django.utils.translation import ugettext_lazy as _
from cms.models import Page
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_subpages.models import SubPage

class SubPagesPlugin(CMSPluginBase):
    model = SubPage
    name = _("Subpages")

    def render(self, context, instance, placeholder):
        # Set template according to plugin template
        self.render_template = 'cmsplugin_subpages/%s' % instance.template

        # Set page ordering
        ordering = instance.order_by
        if instance.order_dir == SubPage.ORDER_ASC:
            ordering = '-%s' % ordering

        # Try to find out page instance by URL
        for page in Page.objects.all().order_by(ordering):
            if page.get_absolute_url() == context['request'].path:
                context['subpages'] = page.get_children()[:instance.amount_pages]

        context['instance'] = instance
        return context

plugin_pool.register_plugin(SubPagesPlugin)