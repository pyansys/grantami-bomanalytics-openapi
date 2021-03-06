import importlib
from .examples import example_dict

models_module = importlib.import_module('ansys.grantami.bomanalytics_openapi.models')


def get_example(model_definition):
    try:
        return example_dict[model_definition.__name__]
    except KeyError:
        return


def generate_model(model_definition):
    example = get_example(model_definition)
    arg_dict = get_arg_dict(example, model_definition)
    return model_definition(**arg_dict)


def get_arg_dict(values, model_class):
    all_types = values.keys()
    complex_types = model_class.subtype_mapping.keys()
    simple_types = [t for t in all_types if t not in complex_types]

    simple_ctor_arguments = {get_python_arg_name(model_class, arg): values[arg] for arg in simple_types}
    complex_ctor_arguments = {get_python_arg_name(model_class, arg): get_complex_arg_value(values, arg, model_class) for arg in complex_types}

    return {**simple_ctor_arguments, **complex_ctor_arguments}


def get_complex_arg_value(values, arg, model_class):
    arg_value = values[arg]
    class_name = model_class.subtype_mapping[arg]
    sub_class = getattr(models_module, class_name)
    if arg_value:
        return [sub_class(**get_arg_dict(example_value, sub_class)) for example_value in arg_value]


def get_python_arg_name(model_class, arg):
    for python_arg, api_arg in model_class.attribute_map.items():
        if api_arg == arg:
            return python_arg
