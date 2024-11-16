_comp_cmd_worky(){
    local config_dir cur suggestions
    config_dir="${DOMO_ROOT:-"$HOME/.config/worky"}"
    cur="${COMP_WORDS[COMP_CWORD]}"
    [[ ! -d "$config_dir" ]] && return 1

    suggestions=$(find "$config_dir" -name "*.toml" -printf "%f\n" | sed -e 's/\.toml$//')
    COMPREPLY=( $(compgen -W "$suggestions" -- "$cur") )
}
complete -F _comp_cmd_worky worky
