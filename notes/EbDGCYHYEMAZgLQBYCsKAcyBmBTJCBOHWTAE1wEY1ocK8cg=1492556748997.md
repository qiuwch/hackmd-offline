# VDL presentation script

## Neonrace

0, drive slowly and try various actions
`python neoncar_trained.py --snapshot train-log/neonrace-snapshot/model.ckpt-0`
after 15 minutes
`python neoncar_trained.py --snapshot train-log/neonrace-snapshot/model.ckpt-6060`
after 30 minutes
`python neoncar_trained.py --snapshot train-log/neonrace-snapshot/model.ckpt-10935`
after 45 minutes
`python neoncar_trained.py --snapshot train-log/neonrace-snapshot/model.ckpt-15055`
after many many hours, almost always straight
`python neoncar_trained.py --snapshot train-log/neonrace-70k/train/model.ckpt-70421`



0
`python neoncar_trained.py --env PongDeterministic-v3 --snapshot  train-log/pong-snapshot/train/model.ckpt-0 --visualise`
after 30 mins
`python neoncar_trained.py --env PongDeterministic-v3 --snapshot  train-log/pong-snapshot/train/model.ckpt-463087 --visualise`
after 60 mins
`python neoncar_trained.py --env PongDeterministic-v3 --snapshot  train-log/pong-snapshot/train/model.ckpt-1063776 --visualise`
after 90 mins
`python neoncar_trained.py --env PongDeterministic-v3 --snapshot  train-log/pong-snapshot/train/model.ckpt-1594208 --visualise`
after 120 mins, slightly better
`python neoncar_trained.py --env PongDeterministic-v3 --snapshot  train-log/pong-snapshot/train/model.ckpt-2165973 --visualise`
after many many hours, overfit
`python neoncar_trained.py --env PongDeterministic-v3 --snapshot train-log/pong1/train/model.ckpt-15075273 --visualise`

