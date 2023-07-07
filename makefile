push:
	sudo git add .
	@read -p "Commit Message : " commit;\
	sudo git commit -m "$$commit"
	sudo git push -u origin master