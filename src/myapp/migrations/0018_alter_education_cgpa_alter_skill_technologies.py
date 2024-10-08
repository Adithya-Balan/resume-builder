# Generated by Django 5.1.1 on 2024-09-22 08:15

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_education_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='CGPA',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='skill',
            name='technologies',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Django', 'Django'), ('react', 'React'), ('angular', 'Angular'), ('vue', 'Vue.js'), ('nodejs', 'Node.js'), ('express', 'Express.js'), ('rails', 'Ruby on Rails'), ('laravel', 'Laravel'), ('symfony', 'Symfony'), ('graphql', 'GraphQL'), ('firebase', 'Firebase'), ('postgresql', 'PostgreSQL'), ('mysql', 'MySQL'), ('sqlite', 'SQLite'), ('mongodb', 'MongoDB'), ('redis', 'Redis'), ('pytorch', 'PyTorch'), ('tensorflow', 'TensorFlow'), ('scikit_learn', 'Scikit-Learn'), ('pandas', 'Pandas'), ('numpy', 'NumPy'), ('opencv', 'OpenCV')], max_length=168),
        ),
    ]
