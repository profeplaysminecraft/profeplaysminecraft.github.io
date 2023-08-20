var textBox = document.createElement("textarea");
textBox.style.width = '100%';
textBox.style.height = '100%';

var identifier = "";
var name = "";
var enchantment = "";
var stack = "";
var nutrition = "";
var saturation = "";
var always_eat = "";
var texture = "";

function getAllValues() {
    identifier = document.getElementById("identifier").value;
    name = document.getElementById("name").value;
    enchantment = document.getElementById("enchantment").value;
    stack = document.getElementById("stack").value;
    nutrition = document.getElementById("nutrition").value;
    saturation = document.getElementById("saturation").value;
    always_eat = document.getElementById("always_eat").value; 
    texture = document.getElementById("texture").value;
};

function createCode() {
    var code_text = `
    {
        "format_version": "1.16.100",
        "minecraft:item": {
            "description": {
                "identifier": "${identifier}",
                  "category": "equipment"
            },
            "components": {
                "minecraft:display_name": {
                    "value": "${name}"
               },
               "minecraft:use_duration": 1.6,
                "minecraft:foil": ${enchantment},
                "minecraft:max_stack_size": ${stack},
                "minecraft:hand_equipped": false,
                "minecraft:stacked_by_data": true,
                "minecraft:icon": {
                    "texture": "${texture}"
                },
                "minecraft:creative_category": {
                    "parent": "itemGroup.name.miscFood"
                },
                "minecraft:food": {
                    "nutrition": ${nutrition},
                    "saturation_modifier": "${saturation}",
                    "can_always_eat": ${always_eat}
                },
                "minecraft:use_animation": "eat"
            }
        }
    }`
    return code_text
};

function addBox() {
    getAllValues();
    let finalCode = createCode();
    var container = document.getElementById("container");
    container.appendChild(textBox);
    textBox.value = finalCode;
}

