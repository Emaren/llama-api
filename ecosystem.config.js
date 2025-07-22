module.exports = {
  apps: [
    {
      name: 'llama-api',
      cwd:  '/var/www/llama-api',

      // ✅ use python to launch uvicorn properly
      script: 'venv/bin/python',
      interpreter: 'none',

      args: [
        '-m', 'uvicorn',
        'backend.main:app',
        '--host',  '127.0.0.1',
        '--port',  '8005',
        '--workers', '1',
        '--proxy-headers',
      ].join(' '),

      exec_mode:   'fork',
      autorestart: true,
      merge_logs:  true,
      log_date_format: 'YYYY-MM-DD HH:mm:ss',

      env: {
        PYTHONUNBUFFERED: '1',
        PYTHONPATH: '/var/www/llama-api',
      },
    },
  ],
};
