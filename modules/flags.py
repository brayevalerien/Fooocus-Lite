from enum import IntEnum, Enum

disabled = 'Disabled'
enabled = 'Enabled'
subtle_variation = 'Vary (Subtle)'
strong_variation = 'Vary (Strong)'
upscale_15 = 'Upscale (1.5x)'
upscale_2 = 'Upscale (2x)'
upscale_fast = 'Upscale (Fast 2x)'

uov_list = [
    disabled, subtle_variation, strong_variation, upscale_15, upscale_2, upscale_fast
]

CIVITAI_NO_KARRAS = ["euler", "euler_ancestral", "heun",
                     "dpm_fast", "dpm_adaptive", "ddim", "uni_pc"]

# fooocus: a1111 (Civitai)
KSAMPLER = {
    "euler": "Euler",
    "euler_ancestral": "Euler a",
    "heun": "Heun",
    "heunpp2": "",
    "dpm_2": "DPM2",
    "dpm_2_ancestral": "DPM2 a",
    "lms": "LMS",
    "dpm_fast": "DPM fast",
    "dpm_adaptive": "DPM adaptive",
    "dpmpp_2s_ancestral": "DPM++ 2S a",
    "dpmpp_sde": "DPM++ SDE",
    "dpmpp_sde_gpu": "DPM++ SDE",
    "dpmpp_2m": "DPM++ 2M",
    "dpmpp_2m_sde": "DPM++ 2M SDE",
    "dpmpp_2m_sde_gpu": "DPM++ 2M SDE",
    "dpmpp_3m_sde": "",
    "dpmpp_3m_sde_gpu": "",
    "ddpm": "",
    "lcm": "LCM"
}

SAMPLER_EXTRA = {
    "ddim": "DDIM",
    "uni_pc": "UniPC",
    "uni_pc_bh2": ""
}

SAMPLERS = KSAMPLER | SAMPLER_EXTRA

KSAMPLER_NAMES = list(KSAMPLER.keys())

SCHEDULER_NAMES = ["normal", "karras", "exponential",
                   "sgm_uniform", "simple", "ddim_uniform", "lcm", "turbo"]
SAMPLER_NAMES = KSAMPLER_NAMES + list(SAMPLER_EXTRA.keys())

sampler_list = SAMPLER_NAMES
scheduler_list = SCHEDULER_NAMES

refiner_swap_method = 'joint'

cn_ip = "Atmosphere"
cn_ip_face = "Face"
cn_canny = "Shapes"
cn_cpds = "Structure"

ip_list = [cn_ip, cn_canny, cn_cpds, cn_ip_face]
default_ip = cn_canny

default_parameters = {
    cn_ip: (0.25, 1),
    cn_ip_face: (0.9, 0.75),
    cn_canny: (0.9, 1),
    cn_cpds: (0.75, .9)
}  # stop, weight

output_formats = ['png', 'jpg', 'webp']

inpaint_engine_versions = ['None', 'v1', 'v2.5', 'v2.6']
inpaint_option_default = 'Inpaint or Outpaint'
inpaint_option_detail = 'Improve Detail (face, hand, eyes, etc.)'
inpaint_option_modify = 'Modify Content'
inpaint_options = [inpaint_option_default,
                   inpaint_option_detail, inpaint_option_modify]

desc_type_photo = 'Photograph'
desc_type_anime = 'Art/Anime'


class MetadataScheme(Enum):
    FOOOCUS = 'fooocus'
    A1111 = 'a1111'


metadata_scheme = [
    (f'{MetadataScheme.FOOOCUS.value} (json)', MetadataScheme.FOOOCUS.value),
    (f'{MetadataScheme.A1111.value} (plain text)', MetadataScheme.A1111.value),
]

lora_count = 3

controlnet_image_count = 2


class Steps(IntEnum):
    QUALITY = 60
    # SPEED = 30
    EXTREME_SPEED = 8


class StepsUOV(IntEnum):
    QUALITY = 36
    # SPEED = 18
    EXTREME_SPEED = 8


class Performance(Enum):
    QUALITY = 'Quality'
    # SPEED = 'Speed'
    # EXTREME_SPEED = 'Draft'

    @classmethod
    def list(cls) -> list:
        return list(map(lambda c: c.value, cls))

    def steps(self) -> int | None:
        return Steps[self.name].value if Steps[self.name] else None

    def steps_uov(self) -> int | None:
        return StepsUOV[self.name].value if Steps[self.name] else None


performance_selections = Performance.list()
