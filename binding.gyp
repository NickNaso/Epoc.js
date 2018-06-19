{
  "targets": [
    {
      "target_name": "index",
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      "sources": [ "epoc.cc"],
      "include_dirs" : [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      "dependencies": [
        "<!(node -p \"require('node-addon-api').gyp\")"
      ],
      'msvs_settings': {
        'VCCLCompilerTool': { 'ExceptionHandling': 1 },
      },
      "conditions": [
        ['OS=="mac"', {
          "cflags": [ "-m64" ],
          "ldflags": [ "-m64" ],
          "xcode_settings": {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'CLANG_CXX_LIBRARY': 'libc++',
            'MACOSX_DEPLOYMENT_TARGET': '10.7',
            "OTHER_CFLAGS": ["-ObjC++"],
            "ARCHS": [ "x86_64" ]
          },
          "link_settings": {
              "libraries": [
                "/Library/Frameworks/edk.framework/edk"
              ],
              "include_dirs": ["./lib/includes/", "./lib/"]
          }
        }]
      ]
    }
  ]
}
