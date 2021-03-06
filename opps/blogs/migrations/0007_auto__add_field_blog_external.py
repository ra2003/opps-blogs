# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Blog.external'
        db.add_column(u'blogs_blog', 'external',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Blog.external'
        db.delete_column(u'blogs_blog', 'external')


    models = {
        u'%s.%s' % (User._meta.app_label, User._meta.module_name): {
            'Meta': {'object_name': User.__name__},
        },
        u'articles.album': {
            'Meta': {'ordering': "['-date_available']", 'object_name': 'Album'},
            u'container_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['containers.Container']", 'unique': 'True', 'primary_key': 'True'}),
            'headline': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'})
        },
        u'articles.post': {
            'Meta': {'ordering': "['-date_available']", 'object_name': 'Post'},
            'albums': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'post_albums'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['articles.Album']"}),
            u'container_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['containers.Container']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'blogs.blog': {
            'Meta': {'ordering': "(u'name',)", 'object_name': 'Blog'},
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'external': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout_mode': ('django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '200'}),
            'main_image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'blank': 'True'}),
            'mirror_site': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'blogs_blog_mirror_site'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['sites.Site']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'related_blogs': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'blog_relatedblogs'", 'to': u"orm['blogs.Blog']", 'through': u"orm['blogs.BlogRelated']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'related_channels': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'blog_relatedchannels'", 'to': u"orm['channels.Channel']", 'through': u"orm['blogs.BlogChannelRelated']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name), 'symmetrical': 'False'})
        },
        u'blogs.blogchannelrelated': {
            'Meta': {'ordering': "(u'order',)", 'object_name': 'BlogChannelRelated'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blogs.Blog']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['channels.Channel']"})
        },
        u'blogs.bloglink': {
            'Meta': {'object_name': 'BlogLink'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'links'", 'to': u"orm['blogs.Blog']"}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'mirror_site': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'blogs_bloglink_mirror_site'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['sites.Site']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        u'blogs.blogpost': {
            'Meta': {'ordering': "[u'-date_available']", 'object_name': 'BlogPost'},
            'accept_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'albums': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'blogpoast_albums'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['articles.Album']"}),
            'audios': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['multimedias.Audio']", 'null': 'True', 'through': u"orm['blogs.BlogPostAudio']", 'blank': 'True'}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blogs.Blog']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blogs.Category']", 'null': 'True', 'blank': 'True'}),
            u'container_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['containers.Container']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'related_blogposts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'blogpost_relatedblogposts'", 'to': u"orm['blogs.BlogPost']", 'through': u"orm['blogs.BlogPostRelated']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['multimedias.Video']", 'null': 'True', 'through': u"orm['blogs.BlogPostVideo']", 'blank': 'True'})
        },
        u'blogs.blogpostaudio': {
            'Meta': {'object_name': 'BlogPostAudio'},
            'audio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multimedias.Audio']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'blogpost': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blogs.BlogPost']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'blogs.blogpostrelated': {
            'Meta': {'ordering': "(u'order',)", 'object_name': 'BlogPostRelated'},
            'blogpost': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'blogpostrelated_blogpost'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['blogs.BlogPost']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'blogpostrelated_related'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['blogs.BlogPost']"})
        },
        u'blogs.blogpostvideo': {
            'Meta': {'object_name': 'BlogPostVideo'},
            'blogpost': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blogs.BlogPost']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multimedias.Video']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        u'blogs.blogrelated': {
            'Meta': {'ordering': "(u'order',)", 'object_name': 'BlogRelated'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'blogrelated_blog'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['blogs.Blog']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'blogrelated_related'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['blogs.Blog']"})
        },
        u'blogs.category': {
            'Meta': {'ordering': "[u'name', u'parent__id', u'published']", 'unique_together': "((u'site', u'blog', u'long_slug'),)", 'object_name': 'Category'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'categories'", 'to': u"orm['blogs.Blog']"}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'long_slug': ('django.db.models.fields.SlugField', [], {'max_length': '250'}),
            'mirror_site': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'blogs_category_mirror_site'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['sites.Site']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "u'subchannel'", 'null': 'True', 'to': u"orm['blogs.Category']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'show_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'channels.channel': {
            'Meta': {'ordering': "[u'name', u'parent__id', u'published']", 'unique_together': "((u'site', u'long_slug', u'slug', u'parent'),)", 'object_name': 'Channel'},
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hat': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_in_main_rss': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '250', 'db_index': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'long_slug': ('django.db.models.fields.SlugField', [], {'max_length': '250'}),
            'main_image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'mirror_site': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'channels_channel_mirror_site'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['sites.Site']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'paginate_by': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "u'subchannel'", 'null': 'True', 'to': u"orm['channels.Channel']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'show_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)}),
        },
        u'containers.container': {
            'Meta': {'ordering': "['-date_available']", 'unique_together': "(('site', 'channel', 'slug'),)", 'object_name': 'Container'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['channels.Channel']"}),
            'channel_long_slug': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'channel_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'child_app_label': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'child_class': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'child_module': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'hat': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['images.Image']", 'null': 'True', 'through': u"orm['containers.ContainerImage']", 'blank': 'True'}),
            'json': ('opps.db.models.fields.jsonf.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'main_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'containers_container_mainimage'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['images.Image']"}),
            'main_image_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mirror_channel': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'containers_container_mirror_channel'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['channels.Channel']"}),
            'mirror_site': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'containers_container_mirror_site'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['sites.Site']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_containers.container_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'related_containers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'container_relatedcontainers'", 'to': u"orm['containers.Container']", 'through': u"orm['containers.ContainerRelated']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'show_on_root_channel': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)}),
        },
        u'containers.containerimage': {
            'Meta': {'ordering': "('order',)", 'object_name': 'ContainerImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['containers.Container']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'containers.containerrelated': {
            'Meta': {'ordering': "('order',)", 'object_name': 'ContainerRelated'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'containerrelated_container'", 'to': u"orm['containers.Container']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'containers_containerrelated_container'", 'to': u"orm['containers.Container']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'images.image': {
            'Meta': {'object_name': 'Image'},
            'archive': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'archive_link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'crop_example': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'crop_x1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_x2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_y1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_y2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fit_in': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'halign': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '6', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mirror_site': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'images_image_mirror_site'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['sites.Site']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'smart': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)}),
            'valign': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '6', 'null': 'True', 'blank': 'True'})
        },
        u'multimedias.audio': {
            'Meta': {'ordering': "[u'-date_available', u'title', u'channel_long_slug']", 'object_name': 'Audio'},
            u'container_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['containers.Container']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'ffmpeg_file_flv': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ffmpeg_file_mp3_128': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ffmpeg_file_mp4_hd': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ffmpeg_file_mp4_sd': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ffmpeg_file_ogv': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ffmpeg_file_thumb': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'local': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "u'local_audio'", 'unique': 'True', 'null': 'True', 'to': u"orm['multimedias.MediaHost']"}),
            'media_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'audio'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['articles.Post']"}),
            'related_posts': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'audio_relatedposts'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['containers.Container']"}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'uolmais': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "u'uolmais_audio'", 'unique': 'True', 'null': 'True', 'to': u"orm['multimedias.MediaHost']"})
        },
        u'multimedias.mediahost': {
            'Meta': {'object_name': 'MediaHost'},
            'embed': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            'host': ('django.db.models.fields.CharField', [], {'default': "u'local'", 'max_length': '16'}),
            'host_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'retries': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "u'notuploaded'", 'max_length': '16'}),
            'status_message': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'updated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True'})
        },
        u'multimedias.video': {
            'Meta': {'ordering': "[u'-date_available', u'title', u'channel_long_slug']", 'object_name': 'Video'},
            u'container_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['containers.Container']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'ffmpeg_file_flv': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ffmpeg_file_mp3_128': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ffmpeg_file_mp4_hd': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ffmpeg_file_mp4_sd': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ffmpeg_file_ogv': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ffmpeg_file_thumb': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'local': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "u'local_video'", 'unique': 'True', 'null': 'True', 'to': u"orm['multimedias.MediaHost']"}),
            'media_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'video'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['articles.Post']"}),
            'related_posts': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'video_relatedposts'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['containers.Container']"}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'uolmais': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "u'uolmais_video'", 'unique': 'True', 'null': 'True', 'to': u"orm['multimedias.MediaHost']"}),
            'vimeo': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "u'vimeo_video'", 'unique': 'True', 'null': 'True', 'to': u"orm['multimedias.MediaHost']"}),
            'youtube': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "u'youtube_video'", 'unique': 'True', 'null': 'True', 'to': u"orm['multimedias.MediaHost']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['blogs']