{
  'targets': [
    {
      'target_name': 'node_stringprep_icu',
      'sources': [ 'node-stringprep-icu.cc' ],
      'cflags!': [ '-fno-exceptions', '`icu-config --cppflags`' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'libraries': [ '`icu-config --ldflags`' ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")'
      ],
      'conditions': [
        ['OS=="freebsd"', {
          'include_dirs': [
              '/usr/local/include'
          ],
        }],
        ['OS=="mac"', {
          'include_dirs': [
              '/opt/local/include'
          ],
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }]
      ]
     }
  ]
}
