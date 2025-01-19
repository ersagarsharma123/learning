# Personal Portfolio Website

A minimal, clean portfolio website with a home page and blog section.

## Local Development

Simply open `index.html` in your web browser to view the website locally.

## Deployment to AWS EC2

1. Connect to your EC2 instance:
```bash
ssh -i C:\Users\sagar\.ssh\ia30_vm_ssh_kp.pem ubuntu@52.66.129.11
```

2. Copy the files to your EC2 instance:
```bash
scp -i C:\Users\sagar\.ssh\ia30_vm_ssh_kp.pem -r index.html blog.html styles.css deploy.sh ubuntu@52.66.129.11:~/
```

3. SSH into your EC2 instance and run the deployment script:
```bash
chmod +x deploy.sh
./deploy.sh
```

4. Visit http://52.66.129.11 in your browser to see the deployed website.

## Structure
- `index.html` - Home page
- `blog.html` - Blog listing page
- `styles.css` - Styling for the website
- `deploy.sh` - Deployment script for AWS EC2

## Customization
1. Update your social media links in `index.html`
2. Add your own blog posts in `blog.html`
3. Modify colors in `styles.css` to match your preferred theme
