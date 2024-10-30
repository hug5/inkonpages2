
# sass options:
  # https://sass-lang.com/documentation/cli/dart-sass/
  # sass --w --style=compressed style.container.scss style.min2.css
  # sass --watch ---poll --style=compressed style.container.scss style.min2.css
  # --no-source-map
  # --update
    # compile stylesheets whose dependencies have been modified more recently than the corresponding CSS file was generated
  # --embed-sources
    # embed the entire contents of the Sass files that contributed to the generated CSS in the source map;
    # this creates a surprisingly very large source file!
  # --embed-source-map
    # embed the contents of the source map file in the generated CSS
    # Thise creates a process css file that is the original + source file; which is only marginally larger;

SCSS="jug/www/static/scss/style.container.scss"
CSS="jug/www/static/css/style.min2.css"

sass --update --no-source-map --style=compressed "$SCSS" "$CSS"
# sass --update --no-source-map --style=compressed "jug/www/static/scss/style.container.scss" "jug/www/static/css/style.min2.css"

# 1 out of 30 chance
DOCM=false
RAND=$((1 + $RANDOM % 30))
# echo $RAND
if [[ RAND -eq 1 ]]; then DOCM=true; fi


# local action:
git add --all
# git commit --amend --allow-empty --no-edit
  # --allow-empty may be necessary if you make a change; commit/push;
  # then reverse that exact change and want to commit/push;
# git commit --amend --no-edit

if [[ $DOCM == false ]]; then echo "gca"; git commit --amend --no-edit; else echo "gcmm"; git commit -m "wip"; fi

git push --force -q
sleep .3

# remote action:
# tmux send-keys -t top "git pull --rebase" enter
# tmux send-keys -t top "url" enter
# tmux send-keys -t ${WINDOW}.${PANE} "git reset HEAD --hard" enter
{remote} "git reset HEAD --hard" enter
  # Undo scss deletes so that we can pull again;
sleep .3
  # Prob. not necessary, but commands are printed out below;
{remote} "git pull --rebase" enter
sleep .3

{remote} "url" enter
sleep .3

{remote} "rm jug/www/static/scss/*" enter
  # Delete the scss folder; but will have to reverse it to git pull again;