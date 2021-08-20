from django import forms
from .models import Image, Join


YEAR_CHOICES = (
    ('1994-1998', '1994-1998'),
    ('1995-1999', '1995-1999'),
    ('1996-2000', '1996-2000'),
    ('1997-2001', '1997-2001'),
    ('1998-2002', '1998-2002'),
    ('1999-2003', '1999-2003'),
    ('2000-2004', '2000-2004'),
    ('2001-2005', '2001-2005'),
    ('2002-2006', '2002-2006'),
    ('2003-2007', '2003-2007'),
    ('2004-2008', '2004-2008'),
    ('2005-2009', '2005-2009'),
    ('2006-2010', '2006-2010'),
    ('2007-2011', '2007-2011'),
    ('2008-2012', '2008-2012'),
    ('2009-2013', '2009-2013'),
    ('2010-2014', '2010-2014'),
    ('2011-2015', '2011-2015'),
    ('2012-2016', '2012-2016'),
    ('2013-2017', '2013-2017'),
    ('2014-2018', '2014-2018'),
    ('2015-2019', '2015-2019'),
    ('2016-2020', '2016-2020'),
    ('2017-2021', '2017-2021'),
    ('2018-2022', '2018-2022'),
    ('2019-2023', '2019-2023'),
    ('2020-2024', '2020-2024'),
)

ATTEND_CHOICES = (
  ('Sẽ tham gia', 'Sẽ tham gia'),
  ('Không tham gia', 'Không tham gia'),
)




class JoinForm(forms.ModelForm):
  name      = forms.CharField(label='Họ tên', widget=forms.TextInput(
                                                      attrs={
                                                        "class": 'form-control form-opacity',
                                                        
                                                      }
                                                    )
                                                  )
  email     = forms.EmailField(label='Email', widget=forms.EmailInput(
                                                      attrs={
                                                        "class": 'form-control form-opacity',
                                                        
                                                      }
                                                    ))
  attend    = forms.CharField(label='Sẽ tham gia?', widget=forms.RadioSelect(choices=ATTEND_CHOICES, attrs={'class': 'list-unstyled', }))
  year      = forms.ChoiceField(choices=YEAR_CHOICES, label='Niên khóa', widget=forms.Select(
                                                      attrs={
                                                        "class": 'form-control form-opacity',
                                                        
                                                      }
                                                    ))
  note      = forms.CharField(label='Ghi chú', widget=forms.Textarea(attrs={
                                                        "class": 'form-control form-opacity',
  }))

  class Meta:
    model = Join
    fields = [
      'name',
      'email',
      'attend',
      'year',
      'note',
]

class ImageForm(forms.ModelForm):
  image      = forms.ImageField(label='Ảnh',widget=forms.FileInput(
                                                        attrs={
                                                        "multiple": True,
                                                        "class": 'form-control form-opacity',

  }))
  year      = forms.ChoiceField(choices=YEAR_CHOICES, label='Niên khóa: ', widget=forms.Select(
                                                        attrs={
                                                          # "class": 'form-control form-opacity',
                                                          
                                                        }
                                                      ))

  class Meta:
    model = Image
    fields = [
      'year',
      'image',
    ]



