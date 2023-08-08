terraform {

    required_version = ">= 1.0.0"
    required_providers {
        aws = {
        source  = "hashicorp/aws"
        version = "~> 5.0"
        }
  }
}

provider " aws" {
    region = "eu-central-1"
    defaul_tags{
        owner = "angemydelson"
        managed-by = "terraform"
    }
  
}